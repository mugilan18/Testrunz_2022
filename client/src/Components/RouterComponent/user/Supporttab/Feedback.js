import React,{useState}from 'react';
import Checkbox from '@mui/material/Checkbox';
import { styled } from '@mui/material/styles';
import Swal from 'sweetalert2'
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Grid from '@mui/material/Grid';
import TextareaAutosize from '@mui/base/TextareaAutosize';
import Button from '@mui/material/Button';
import { useStateValue } from '../../../../data/StateProvider';
import Rating from '@mui/material/Rating';
import ApiUrl from "../../../../ServerApi";
import axios from "axios";

const Input = styled('input')({
  display: 'none',
});


const Feedback = () => {
  const[feedback,setFeedback]=useState("")
  // const[rating,setRating]=useState(0)
  const [baseImage, setBaseImage] = useState("");
const [type,setType]=useState("");

  const [{ user }, dispatch] = useStateValue();

  const uploadImage = async (e) => {
    const file = e.target.files[0];
    const base64 = await convertBase64(file);
    setBaseImage(base64);
  };

  const convertBase64 = (file) => {
    return new Promise((resolve, reject) => {
      const fileReader = new FileReader();
      fileReader.readAsDataURL(file);

      fileReader.onload = () => {
        resolve(fileReader.result);
      };

      fileReader.onerror = (error) => {
        reject(error);
      };
    });
  };

  const sendfeedback =(e)=>{
    e.preventDefault();
    if(!type){
      alert("enter the type")
          }
    else if(!feedback){
alert("enter some content")
    }
    else{
    axios.post(`${ApiUrl}/feedback`, {
      postedby:user.email,
        type:type,
        feedback:feedback,
        image:baseImage,
    }).then((res)=>{
      console.log("feedback sent")
      setBaseImage("")
      setFeedback("")
      setType("")
      Swal.fire(
        'success',
        'your feedback has been Submitted',
        'success',
      )
    }).catch((err)=>{
      console.log(err)
    })

    // console.log(rating)
    // console.log(feedback)
    // console.log(user)

    setFeedback("")
    // setRating(0)
    setType("")
  }}
  return (
    <Card>
    <CardContent style={{backgroundColor:"#E7EBF0"}}>
  
    <p><span style={{fontWeight:"bold"}}>Feedback </span >&nbsp;&nbsp;&nbsp;<span style={{color:"#595958"}}>"Help us to improve"</span></p>
    <br/> <br/> 
    <FormControl>
  <FormLabel id="demo-radio-buttons-group-label">Category</FormLabel>
  <RadioGroup
  row
    aria-labelledby="demo-radio-buttons-group-label"
    defaultValue="female"
    name="radio-buttons-group"
    value={type}
    onChange={(e)=>setType(e.target.value)}
  >
    <FormControlLabel value="bug" control={<Radio />} label="Bug" />
    <FormControlLabel value="feature" control={<Radio />} label="Features" />
    <FormControlLabel value="others" control={<Radio />} label="Others" />
  </RadioGroup>
</FormControl>

<br/><br/> 
    <TextareaAutosize
      aria-label="minimum height"
      minRows={6}
      placeholder="  Enter Your Feedback....."
      style={{ width: 500 }}
      value={feedback}
      onChange={(e)=>setFeedback(e.target.value)}
    />
    <br/>  <br/>  
   {/* <Grid container spacing={2}>
   <Grid item>
  <p><span style={{fontWeight:"bold"}}>Rate Us : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span ></p>

  </Grid> 
  <Grid item >
  <Rating name="half-rating" value={rating} onChange={(e)=>setRating(e.target.value)} precision={0.5} />

  </Grid>
  </Grid>*/}
  <img src={baseImage} height="200px" />
  <br/>
  <br/>

  <label htmlFor="contained-button-file">
        <Input accept="image/*" id="contained-button-file" multiple type="file"  
        onChange={(e) => {
          uploadImage(e);
        }}/>
        <Button variant="contained" style={{ backgroundColor:"#F1C232",color:"black" }} component="span">
          Upload
        </Button>
      </label>

    <br/>  <br/>  

    <Button variant="contained"  style={{ backgroundColor:"#F1C232",color:"black" }} onClick={sendfeedback}>Submit</Button>  
  
    </CardContent>
    </Card>
  );
};

export default Feedback;
