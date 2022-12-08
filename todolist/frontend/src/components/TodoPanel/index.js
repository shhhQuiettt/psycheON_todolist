import React from "react";
import AddTaskForm from "../AddTaskForm";
import { Paper } from "@mui/material";
import TodoList from "../TodoList";
import Box from "@mui/material/Box";
import { fetchAllTasks } from "../../service";
import { useState, useEffect } from "react";
import ConnectionError from "../Alerts/ConnectionError";

const TodoPanel = () => {
  const [tasks, setTasks] = useState([]);
  const [connectionError, setConectionError] = useState(false);

  const refreshTasks = async () => {
    try {
      const data = await fetchAllTasks();
      setTasks(data);
    } catch (error) {
      if (error.message === "Connection Error") {
        setConectionError(true);
      }
    }
  };

  useEffect(() => {
    refreshTasks();
  }, []);

  return (
    <Box>
      <AddTaskForm afterSubmit={() => refreshTasks()} />
      {connectionError && <ConnectionError />}
      <Paper>
        <TodoList tasks={tasks} refreshTasks={refreshTasks} />
      </Paper>
    </Box>
  );
};

export default TodoPanel;
