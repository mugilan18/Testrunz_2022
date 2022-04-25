import React,{useEffect} from "react";
// import NavBar from "./Components/NavBar/NavBar";
import AppRouter from "./Components/RouterComponent/RouterComponent";
import { useStateValue } from './data/StateProvider';
import {actionTypes} from "./data/reducer"
import { useCookies } from "react-cookie";
import axios from "axios";
import { Redirect } from "react-router-dom";

function App() {
  const [{ user }, dispatch] = useStateValue();

  const [cookies, setCookie, removeCookie] = useCookies(["userjwt"]);
  useEffect(()=>{
  
    async function fetchuserData() {
      
      await axios
        .post(`${process.env.REACT_APP_API}/validateuser`, {
          usertoken: cookies.userjwt
        })
        .then((res) => {
          
          
          dispatch({
            type: actionTypes.SET_USER,
            user: res.data.user
         });
         if(res.data.user.showOnce===false){
          // <Redirect to="/private" />
          console.log("true",res.data.user.showOnce)
         }
        //  if(res.data.user.showOnce===true){
        //    <Redirect to="/app" />
        //   console.log("true")
        //  }

        

         });
    }

    fetchuserData();

  },[])

  return (
    <div>
      {/* <NavBar /> */}
      <AppRouter user={ user }/>
    </div>
  );
}

export default App;
