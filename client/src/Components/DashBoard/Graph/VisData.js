import axios from "axios";
import ApiUrl from "../../../ServerApi";


const fetch1 = async function () {
  let result = await axios
    .get(`${ApiUrl}/runPython/test`)
    .then((res) => res.data);
  //console.log(result);
  return result;
};

export default fetch1;
