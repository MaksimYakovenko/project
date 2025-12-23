import axios from "axios";

const apiPublic = axios.create({
  baseURL: "/api",
  withCredentials: true
});

export default apiPublic;