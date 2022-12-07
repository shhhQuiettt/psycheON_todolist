from django.test import TestCase
from django.urls.exceptions import NoReverseMatch
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Task
from django.db import models
from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

# Create your tests here.
class TaskModelTest(TestCase):
    # Explicit a task
    def test_task_model_has_proper_fields(self):
        task_fields = {
            "id": models.IntegerField,
            "title": models.CharField,
            "done": models.BooleanField,
            "author_ip": models.CharField,
            "created_date": models.DateField,
            "done_date": models.DateField,
        }

        task = Task.objects.create()
        for field, field_type in task_fields.items():
            with self.subTest(field=field):
                self.assertIsInstance(task._meta.get_field(field), field_type)


class TasksListApiTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.task_list_view_name = "task-list"

        cls.retrieve_fields = {
            "id",
            "title",
            "done",
            "author_ip",
            "created_date",
            "done_date",
        }

        cls.client_ip = "10.0.0.14"
        cls.client = APIClient(
            HTTP_X_FORWARDED_FOR=cls.client_ip, REMOTE_ADDR=cls.client_ip
        )

        super().setUpClass()

    @classmethod
    def setUpTestData(cls):
        cls.tasks = [
            Task.objects.create(
                title="ąęćłasdf",
                done=False,
                author_ip="10.0.0.4",
                created_date=(timezone.now() - timedelta(days=9)).date(),
                done_date=(timezone.now() - timedelta(days=6)).date(),
            ),
            Task.objects.create(
                title="ąęćłasdf",
                done=False,
                author_ip="10.0.0.4",
                created_date=timezone.now() - timedelta(days=1),
            ),
        ]

    # Explicit b task test
    def test_list_endpoint_exists(self):
        try:
            reverse(self.task_list_view_name)
        except NoReverseMatch:
            self.fail(f"{self.task_list_view_name} does not exist")

    # Explicit b task test
    def test_list_view_returns_list_of_task(self):
        url = reverse(self.task_list_view_name)
        res = self.client.get(url)

        returned_ids = [t.get("id") for t in res.data]

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(self.tasks))

        self.assertIn(self.tasks[0].id, returned_ids)
        self.assertIn(self.tasks[1].id, returned_ids)

    # Explicit c task
    def test_creating_task_without_done_and_done_date_creates_task(self):
        url = reverse(self.task_list_view_name)
        req_data = {"title": "Do the laundry"}
        prev_tasks_count = Task.objects.count()

        res = self.client.post(url, req_data)
        new_tasks_count = Task.objects.count()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_tasks_count, prev_tasks_count + 1)

    # Explicit c task
    def test_creating_task_without_done_and_done_date_sets_proper_fiels(self):
        """Sets done field to false, and done_date to None"""

        url = reverse(self.task_list_view_name)
        req_data = {"title": "Do the laundry"}

        res = self.client.post(url, req_data)

        task = Task.objects.get(pk=res.data.get("id"))

        self.assertFalse(task.done)
        self.assertIsNone(task.done_date)

    # Explicit task c
    def test_creating_task_with_done_true_without_done_date_creates_task(self):
        url = reverse(self.task_list_view_name)
        req_data = {"title": "Do more laundry", "done": True}
        prev_tasks_count = Task.objects.count()

        res = self.client.post(url, req_data)
        new_tasks_count = Task.objects.count()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_tasks_count, prev_tasks_count + 1)

    # Explicit task c
    def test_creating_task_with_done_true_without_done_date_sets_proper_fields(self):
        """Sets done field to True, and done_date to currant_date"""

        url = reverse(self.task_list_view_name)
        req_data = {"title": "Do the laundry", "done": True}

        res = self.client.post(url, req_data)

        task = Task.objects.get(pk=res.data.get("id"))

        self.assertTrue(task.done)
        self.assertEqual(task.done_date, timezone.now().date())

    # Explicit c task
    def test_creating_task_with_done_true_with_done_date_creates_task(self):
        url = reverse(self.task_list_view_name)
        done_date = (timezone.now() - timedelta(days=3)).date()
        req_data = {"title": "Do more laundry", "done": True, "done_date": done_date}
        prev_tasks_count = Task.objects.count()

        res = self.client.post(url, req_data)
        new_tasks_count = Task.objects.count()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(new_tasks_count, prev_tasks_count + 1)

    # Explicit c task
    def test_creating_task_with_done_true_without_done_date_sets_proper_fiels(self):
        """Sets done field to True, and done_date to given done_date"""

        url = reverse(self.task_list_view_name)
        done_date = (timezone.now() - timedelta(days=3)).date()
        req_data = {"title": "Do the laundry", "done": True, "done_date": done_date}

        res = self.client.post(url, req_data)

        task = Task.objects.get(pk=res.data.get("id"))

        self.assertTrue(task.done)
        self.assertEqual(task.done_date, done_date)

    # Explicit c task
    def test_creating_task_with_invalid_done_done_date_pairs_unallowed(self):
        url = reverse(self.task_list_view_name)

        invalid_pairs = [
            {"done": False, "done_date": timezone.now().date()},
            {"done": False, "done_date": "yesterday"},
        ]

        for pair in invalid_pairs:
            with self.subTest(pair=pair):
                prev_tasks_count = Task.objects.count()
                req_data = {"title": "Do more laundry", **pair}

                res = self.client.post(url, req_data)
                new_tasks_count = Task.objects.count()

                self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(new_tasks_count, prev_tasks_count)

    def test_creating_task_sets_author_ip_properly(self):
        url = reverse(self.task_list_view_name)
        req_data = {"title": "Do the laundry", "done": True}

        client_ip = "10.0.0.4"
        res = self.client.post(url, req_data, HTTP_X_FORWARDED_FOR=client_ip)
        task = Task.objects.get(pk=res.data.get("id"))

        self.assertTrue(task.done)
        self.assertEqual(task.author_ip, client_ip)


class TasksDetailApiTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.task_detail_view_name = "task-detail"

        cls.retrieve_fields = {
            "id",
            "title",
            "done",
            "author_ip",
            "created_date",
            "done_date",
        }

        cls.client_ip = "10.0.0.14"
        cls.client = APIClient(HTTP_X_FORWARDED_FOR=cls.client_ip)

        super().setUpClass()

    @classmethod
    def setUpTestData(cls):
        cls.task1 = Task.objects.create(
            title="ąęćłasdf",
            done=False,
            author_ip="10.0.0.4",
            created_date=(timezone.now() - timedelta(days=9)).date(),
            done_date=None,
        )
        cls.task2 = Task.objects.create(
            title="Do things",
            done=True,
            author_ip="10.0.0.4",
            created_date=(timezone.now() - timedelta(days=9)).date(),
            done_date=(timezone.now() - timedelta(days=6)).date(),
        )

    # Explicit d task test
    def test_detail_endpoint_exists(self):
        try:
            reverse(self.task_detail_view_name, kwargs={"pk": 3})
        except NoReverseMatch:
            self.fail(f"{self.task_detail_view_name} does not exist")

    # Explicit task d
    def test_retrieving_task_possible_if_id_exists_and_returns_proper_fields(self):
        task_id = self.task1.id
        url = reverse(self.task_detail_view_name, kwargs={"pk": task_id})

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(set(res.data.keys()), self.retrieve_fields)

    # Explicit task d
    def test_retrieving_task_with_unknown_id_returns_404(self):
        task_id = self.task1.id + self.task2.id
        url = reverse(self.task_detail_view_name, kwargs={"pk": task_id})

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    # Explicit task e
    def test_deleting_task_possible_if_id_exists(self):
        task_id = self.task1.id
        url = reverse(self.task_detail_view_name, kwargs={"pk": task_id})

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(id=task_id).count(), 0)

    # Explicit task e
    def test_deleting_task_with_unknown_id_returns_404(self):
        task_id = self.task1.id + self.task2.id
        url = reverse(self.task_detail_view_name, kwargs={"pk": task_id})

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_updating_task_possible_if_id_exists(self):
        task_id = self.task1.id
        url = reverse(self.task_detail_view_name, kwargs={"pk": task_id})

        updated_data = {
            "title": "new title",
        }

        res = self.client.put(url, updated_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.get(id=task_id).title,
            updated_data["title"],
        )

    def test_updating_task_with_unknown_id_returns_404(self):
        task_id = self.task1.id + self.task2.id
        url = reverse(self.task_detail_view_name, kwargs={"pk": task_id})

        res = self.client.put(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_toggling_done_to_true_sets_current_date_as_done_date(self):
        undone_task = Task.objects.create(
            title="123",
            done=False,
            author_ip="10.0.0.4",
            created_date=(timezone.now() - timedelta(days=9)).date(),
            done_date=None,
        )
        url = reverse(self.task_detail_view_name, kwargs={"pk": undone_task.id})

        updated_data = {"done": True}

        res = self.client.patch(url, updated_data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(
            Task.objects.get(id=undone_task.id).done,
        )
        self.assertEqual(
            Task.objects.get(id=undone_task.id).done_date, timezone.now().date()
        )
