import axios from "axios";
import ApiUrl from "../../../ServerApi";

let labV = null;

const result = axios.get(`${ApiUrl}/labrotories`).then((result) => result.data);

const test = result.then((res) => {
  const index = res.map((item) =>
    Object.keys(item).filter((value) => value !== "_id" && value !== "__v")
  );
  labV = index[0].map((val) => ({ text: val, value: val }));
  return labV;
});

async function lab() {
  let result = await test;
  return result;
}

export const laboratries = lab().then((res) => res);
