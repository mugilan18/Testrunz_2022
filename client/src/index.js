import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css";
import reportWebVitals from "./reportWebVitals";
import { StateProvider } from '../src/data/StateProvider'
import reducer, { initialState } from '../src/data/reducer'
import { CookiesProvider } from "react-cookie";
ReactDOM.render(
  <React.StrictMode>
    <CookiesProvider>
    <StateProvider initialState={initialState}
      reducer={reducer}>
    
        <App />
    
    </StateProvider>
    </CookiesProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();








