import React from "react";
import AddTaskForm from "../AddTaskForm";
import { Paper } from "@mui/material";
import TodoList from "../TodoList";
import Box from "@mui/material/Box";
import { fetchAllTasks } from "../../service";
import { useState, useEffect } from "react";

const TodoPanel = () => {
  const [tasks, setTasks] = useState([]);

  const refreshTasks = async () => {
    const data = await fetchAllTasks();
    setTasks(data);
  };

  useEffect(() => {
    refreshTasks();
  }, []);

  return (
    <Box>
      <AddTaskForm afterSubmit={() => refreshTasks()} />
      <Paper>
        <TodoList tasks={tasks} refreshTasks={refreshTasks} />
      </Paper>
    </Box>
  );
};

export default TodoPanel;
