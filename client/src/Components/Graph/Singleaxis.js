


import { Button } from '@mui/material';
import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

import { v4 as uuidv4 } from 'uuid';

import "./Graph.css"
function Singleaxis() {

  const [inputFields, setInputFields] = useState([
    { id: uuidv4(), x1: "", y1: "" },
  ]);
const[maxval,setMaxval]=useState()
const[temp,setTemp]=useState()



  const generate = () => {
    setTemp()
    let yval = inputFields.map((obj) => obj.y1);
   let newyval= yval.map(Number);
   setMaxval(Math.max(...newyval) )
    setTemp(inputFields)
    // setData(!temp)
    console.log("InputFields", inputFields);
    
  };

  const handleChangeInput = (id, event) => {
    const newInputFields = inputFields.map(i => {
      if(id === i.id) {
        i[event.target.name] = event.target.value
      }
      return i;
    })
    
    setInputFields(newInputFields);
    if(inputFields[inputFields.length - 1].id===id){
      setInputFields([...inputFields, { id: uuidv4(),  x1: "", y1: "" }])    }
  }

  const handleAddFields = () => {
    setInputFields([...inputFields, { id: uuidv4(),  x1: "", y1: "" }])
  }

  const handleRemoveFields = id => {
    const values  = [...inputFields];
    values.splice(values.findIndex(value => value.id === id), 1);
    setInputFields(values);
  }

  return (
    <div>
      <h1>Simple line Graph</h1>
      <table >
      <thead>
  <tr>
    <th>XAxis</th>
    <th>YAxis</th>
    <th>Remove cell</th>
  
  </tr>

  </thead>
  <tbody>
        { inputFields.map(inputField => (
         
          
            <tr key={inputField.id}>
              <td>
            <input
              name="x1"
              style={{width:"100px"}}
              value={inputField.x}
              onChange={event => handleChangeInput(inputField.id, event)}
            />
            </td>
            <td>
              
            <input
              name="y1"
              style={{width:"100px"}}
              value={inputField.y1}
              onChange={event => handleChangeInput(inputField.id, event)}
            />
            </td>
            <td>
              
            <button disabled={inputFields.length === 1} onClick={() => handleRemoveFields(inputField.id)}>
              remove
            </button>
            </td>
           
            </tr>
        
        )) }
  </tbody>

</table>
<br/>


        <Button
        variant='contained'
          onClick={()=>generate()}
        >Generate</Button>
     
      <br/>

   <div>
      {/* <LineChart width={600} height={300} data={data}>
    <Line  dataKey="y1" stroke="#8884d8" />
    <CartesianGrid stroke="#ccc" />
    <XAxis dataKey="x1" />
    <YAxis />
  </LineChart>    */}
{temp&&
  <ResponsiveContainer width="50%" aspect={2}>
        <LineChart
          width={500}
          height={300}
          data={temp}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="x1" />
          <YAxis dataKey='y1' domain={[0, maxval]} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="y1" stroke="#8884d8" activeDot={{ r: 8 }} />
          {/* <Line type="monotone" dataKey="uv" stroke="#82ca9d" /> */}
        </LineChart>
      </ResponsiveContainer>
      }

</div>

    </div>
  );
}

export default Singleaxis;
