console.clear();
import express from "express";
import { WEB_PORT } from "./files/serverConsts";
import routing from "./files/routing";
import "./files/websockets";

const app = express();

app.use(routing);

app.listen(WEB_PORT, () => console.log(`Web server listening on port ${WEB_PORT}`));

export default app;
