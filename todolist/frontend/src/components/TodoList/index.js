import React from "react";
import {
  Table,
  TableBody,
  TableHead,
  TableCell,
  TableRow,
  TableContainer,
  Typography,
} from "@mui/material";
import ButtonsPanel from "../ButtonsPanel";
import { useState, useEffect } from "react";
import TableRowForm from "../TableRowForm";
import ServerError from "../Alerts/ServerError";
import Checkbox from "@mui/material/Checkbox";
import { toggleDone, deleteTask } from "../../service";
import PropTypes from "prop-types";

const TodoList = ({ tasks, refreshTasks }) => {
  const [editedTaskId, setEditedTaskId] = useState();

  useEffect(() => {
    refreshTasks();
  }, [editedTaskId]);

  return (
    <TableContainer>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>No.</TableCell>
            <TableCell>Title</TableCell>
            <TableCell align="center">Done date</TableCell>
            <TableCell align="center">Done</TableCell>
            <TableCell align="center">Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {tasks.map((row, rowIndex) =>
            row.id === editedTaskId ? (
              <TableRowForm
                key={row.id}
                rowNumber={rowIndex}
                rowData={row}
                onSuccess={() => {
                  setEditedTaskId(null);
                }}
              />
            ) : (
              <TableRow key={row.id}>
                <TableCell>{rowIndex + 1}</TableCell>
                <TableCell>
                  <Typography
                    sx={
                      row.done && {
                        textDecoration: "line-through",
                        color: "gray",
                      }
                    }
                  >
                    {row.title}
                  </Typography>
                  {/* {row.title} */}
                </TableCell>
                <TableCell align="center">{row.done_date}</TableCell>
                <TableCell align="center">
                  <Checkbox
                    color="success"
                    checked={row.done}
                    onChange={() => {
                      toggleDone(row.id, row.done).then(() => refreshTasks());
                    }}
                  />
                </TableCell>
                <TableCell>
                  <ButtonsPanel
                    onEdit={() => {
                      setEditedTaskId(row.id);
                    }}
                    onDelete={() => {
                      deleteTask(row.id).then(refreshTasks);
                    }}
                  />
                </TableCell>
              </TableRow>
            )
          )}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

TodoList.propTypes = {
  data: PropTypes.arrayOf(PropTypes.object),
  refreshTasks: PropTypes.func,
};
export default TodoList;
