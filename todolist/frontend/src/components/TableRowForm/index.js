import React, { useEffect, useState } from "react";
import { TableRow, Table, TableCell, Button } from "@mui/material";
import { DesktopDatePicker } from "@mui/x-date-pickers/DesktopDatePicker";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";
import Checkbox from "@mui/material/Checkbox";
import TextField from "@mui/material/TextField";
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs";
import dayjs from "dayjs";
import EditIcon from "@mui/icons-material/Edit";
import { updateTask } from "../../service";
import PropTypes from "prop-types";

const TableRowForm = ({ rowData, rowNumber, onSuccess }) => {
  const onSubmit = async () => {
    await updateTask(formData);
    onSuccess();
  };

  const [formData, setFormData] = useState({
    id: rowData.id,
    title: rowData.title,
    done: rowData.done,
    done_date: rowData.done_date,
  });

  const handleFieldChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });
  return (
    <>
      <TableRow key={rowData.id}>
        <TableCell>{rowNumber + 1}</TableCell>
        <TableCell>
          <TextField
            form="task-edit-form"
            size="small"
            name="title"
            label="Title"
            fullWidth
            value={formData.title}
            onChange={handleFieldChange}
            placeholder="Task title"
            variant="outlined"
          />
        </TableCell>

        <TableCell>
          <LocalizationProvider dateAdapter={AdapterDayjs}>
            <DesktopDatePicker
              label="Done date"
              inputFormat="YYYY-MM-DD"
              value={
                formData.done
                  ? dayjs(formData.done_date, "YYYY-MM-DD")
                  : dayjs()
              }
              onChange={(v) => {
                setFormData({
                  ...formData,
                  done_date: v?.format("YYYY-MM-DD"),
                });
              }}
              renderInput={(params) => <TextField size="small" {...params} />}
              disabled={!formData.done}
            />
          </LocalizationProvider>
        </TableCell>

        <TableCell>
          <Checkbox
            name="done"
            checked={formData.done}
            onChange={(e) => {
              setFormData({
                ...formData,
                done_date: !formData.done ? formData.done_date : null,
                done: !formData.done,
              });
            }}
          />
        </TableCell>

        <TableCell>
          <Button
            type="submit"
            variant="contained"
            endIcon={<EditIcon />}
            onClick={onSubmit}
          >
            Save
          </Button>
        </TableCell>
      </TableRow>
    </>
  );
};

TableRowForm.propTypes = {
  onSuccess: PropTypes.func,
  rowData: PropTypes.object,
  rowNumber: PropTypes.number,
};
export default TableRowForm;
