import axios from "axios";

const apiPrivate = axios.create({
  baseURL: "/api",
  withCredentials: true
});

export function setAccessTokenToHeaders(token) {
  if (token) {
    apiPrivate.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    delete apiPrivate.defaults.headers.common["Authorization"];
  }
}

export default apiPrivate;