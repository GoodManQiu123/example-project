import axios from "axios";
import router from "@/router";

// create a new axios instance
const sysInstance = axios.create({
  baseURL: import.meta.env.VITE_BASE_API,
});

// request interceptor
sysInstance.interceptors.request.use(
  (config) => {
    // add config here if needed
    return config;
  },
  // if the request is not successful, it will be caught by the catch block and redirected to the error page
  (error) => {
    console.log('Error Message:', error)
    router.push({path: '/error', query: { msg: error }}).then();
    return Promise.reject(error);
  }
);

// response interceptor
sysInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  // if the response is not successful, it will be caught by the catch block and redirected to the error page
  (error) => {
    console.log('Error Message:', error)
    router.push({path: '/error', query: { msg: error }}).then();
    return Promise.reject(error);
  }
);

const sysMethods = ['get', 'post', 'put', 'delete', 'patch'];
const req = {};
sysMethods.forEach((method) => {
  req[method] = (url, paramsOrData) => {
    // if the method is get or delete, the parameters are passed through the params attribute, otherwise they are passed through the data attribute
    const config = { url, method };
    if (method === 'get' || method === 'delete') {
      config.params = paramsOrData;
    } else {
      config.data = paramsOrData;
    }
    return sysInstance(config);
  }
});

export default req;
