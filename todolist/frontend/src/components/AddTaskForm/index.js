import React from "react";
import { TextField, Button } from "@mui/material";
import { useState } from "react";
import IconButton from "@mui/material/IconButton";
import AddIcon from "@mui/icons-material/Add";
import Box from "@mui/material/Box";
import { createTask } from "../../service";
import { PropTypes } from "prop-types";

const AddTaskForm = ({ afterSubmit }) => {
  const [taskTitle, setTaskTitle] = useState("");

  const onSubmit = async (e) => {
    e.preventDefault();
    const data = { title: taskTitle, done: false };
    await createTask(data);
    afterSubmit();
    setTaskTitle("");
  };

  return (
    <Box
      component="form"
      mb={2}
      sx={{ display: "flex", justifyContent: "center" }}
      onSubmit={onSubmit}
    >
      <TextField
        name="title"
        id="title"
        label="What do you want to do?"
        variant="standard"
        value={taskTitle}
        onChange={(e) => setTaskTitle(e.target.value)}
        sx={{ width: "70%" }}
        required
      />
      <IconButton type="submit">
        <AddIcon />
      </IconButton>
    </Box>
  );
};

AddTaskForm.propTypes = {
  afterSubmit: PropTypes.func,
};
export default AddTaskForm;
