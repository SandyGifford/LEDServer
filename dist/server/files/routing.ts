import express from "express";
import path from "path";
import { BUILD_PATH, WS_PORT } from "./serverConsts";

const app = express();

app.get("/wsPort", (req, res) => res.json({ wsPort: WS_PORT }))
app.get("*", express.static(path.join(BUILD_PATH)));

export default app;
