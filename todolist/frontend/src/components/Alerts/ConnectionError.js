import React from "react";
import AlertTitle from "@mui/material/AlertTitle";
import PropTypes from "prop-types";
import Alert from "@mui/material/Alert";

const ConnectionError = ({ message }) => {
  return (
    <Alert severity="error">
      <AlertTitle>Connection error</AlertTitle>
      {message ? message : "Couldn't connect to the server"}
    </Alert>
  );
};

ConnectionError.propTypes = {
  message: PropTypes.string,
};

export default ConnectionError;
