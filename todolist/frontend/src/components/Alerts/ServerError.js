import React from "react";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";

const ServerError = () => {
  return (
    <Alert severity="error">
      <AlertTitle>Server Error</AlertTitle>
      An unexpected error occurred. Try again later.
    </Alert>
  );
};

export default ServerError;
