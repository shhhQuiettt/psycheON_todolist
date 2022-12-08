import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const updateTask = async (data) => {
  try {
    await axios.put(`${API_URL}/todolist/${data.id}/`, data);
  } catch (error) {
    console.error(error);
  }
};

export const fetchAllTasks = async () => {
  try {
    const res = await axios.get(`${API_URL}/todolist/`);
    return res.data;
  } catch (error) {
    console.error(error);
    if (!error.response && error.request) {
      throw Error("Connection Error");
    }
  }
};

export const toggleDone = async (taskId, done) => {
  try {
    await axios.patch(`${API_URL}/todolist/${taskId}/`, {
      done: !done,
      done_date: null,
    });
  } catch (error) {
    console.error(error);
  }
};

export const deleteTask = async (taskId) => {
  try {
    await axios.delete(`${API_URL}/todolist/${taskId}`);
  } catch (error) {
    console.error(error);
  }
};

export const createTask = async (data) => {
  try {
    await axios.post(`${API_URL}/todolist/`, { ...data });
  } catch (error) {
    console.error(error);
  }
};
