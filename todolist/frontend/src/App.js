import React from "react";
import { Typography } from "@mui/material";
import TodoPanel from "./components/TodoPanel";
import Container from "@mui/material/Container";

const App = () => {
  return (
    <Container maxWidth="lg">
      <Typography variant="h2">Todo list</Typography>
      <TodoPanel />
    </Container>
  );
};

export default App;
