import React from "react";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import PropTypes from "prop-types";

const ServerError = ({ message }) => {
  return (
    <Alert severity="error">
      <AlertTitle>Server Error</AlertTitle>
      {message ? message : "An unexpected error occurred. Try again later."}
    </Alert>
  );
};

ServerError.propTypes = {
  message: PropTypes.string,
};

export default ServerError;
