import axios from "axios"

const googleLogin = async (accesstoken) => {
    let res = await axios.get(
      "http://localhost:8000/accounts/login",
      {
        access_token: accesstoken,
      }
    );
    console.log(res);
    return await res.status;
  };

export default googleLogin;