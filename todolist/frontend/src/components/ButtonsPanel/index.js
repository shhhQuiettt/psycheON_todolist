import { ButtonGroup, IconButton } from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import React from "react";

const ButtonsPanel = ({ onEdit, onDelete }) => {
  return (
    <ButtonGroup variant="outlined">
      <IconButton onClick={onEdit} aria-label="edit">
        <EditIcon />
      </IconButton>
      <IconButton onClick={onDelete} aria-label="delete">
        <DeleteIcon />
      </IconButton>
    </ButtonGroup>
  );
};

export default ButtonsPanel;
