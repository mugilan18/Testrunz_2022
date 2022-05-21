import axios from "axios";
import ApiUrl from "../ServerApi";

const USER_API_BASE_URL = `${ApiUrl}/experiments`;
const USER_API_BASE = `${ApiUrl}`;

class ApiService {
  fetchUsers(userId) {
    console.log("dadasdas",userId)
    return axios.get(USER_API_BASE_URL+ "/runz/"+userId._id);
  }
  fetchUsersmail(usermail) {
   console.log("dadasdas",usermail)
    return axios.post(USER_API_BASE_URL+ "/mypage",usermail);
  }

  fetchUserById(userId) {
    return axios.get(USER_API_BASE_URL + "/" + userId);
  }

  deleteUser(userId) {
    return axios.delete(USER_API_BASE_URL + "/" + userId);
  }

  addUser(user) {
    return axios.post("" + USER_API_BASE_URL, user);
  }

  addBulkuser(user) {
    return axios.post("" + USER_API_BASE_URL+"/bulk", user);
  }

  editUser(user) {
    return axios.patch(USER_API_BASE_URL + "/" + user._id, user);
  }
  removeshareduser(user) {
    return axios.patch(USER_API_BASE_URL + "/remove/" + user._id, user);
  }
  mailUser(user) {
    return axios.post(USER_API_BASE_URL + "/mail", user);
  }
  AllUser() {
    return axios.get(USER_API_BASE);
  }
}

export default new ApiService();
