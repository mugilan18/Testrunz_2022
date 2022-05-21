import { Button } from "@mui/material";
import React, { useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

import { v4 as uuidv4 } from "uuid";
import "./Graph.css"
function Multiaxis() {
  const [inputFields, setInputFields] = useState([
    { id: uuidv4(), x1: "", y1: "", y2: "", y3: "", y4: "" },
  ]);
  const [maxval1, setMaxval1] = useState();
  const [maxval2, setMaxval2] = useState();
  const [maxval3, setMaxval3] = useState();
  const [maxval4, setMaxval4] = useState();

  const [temp, setTemp] = useState();
  const [column, setColumn] = useState();

  const generate = () => {
    setTemp();
    let yval1 = inputFields.map((obj) => obj.y1);
    let yval2 = inputFields.map((obj) => obj.y2);
    let yval3 = inputFields.map((obj) => obj.y3);
    let yval4 = inputFields.map((obj) => obj.y4);

    let newyval1 = yval1.map(Number);
    let newyval2 = yval2.map(Number);
    let newyval3 = yval3.map(Number);
    let newyval4 = yval4.map(Number);

    // let ylist = [...newyval1,...newyval2,...newyval3,...newyval4]
    setMaxval1(Math.max(...newyval1));
    setMaxval2(Math.max(...newyval2));
    setMaxval3(Math.max(...newyval3));
    setMaxval4(Math.max(...newyval4));

    setTemp(inputFields);
    // setData(!temp)
    console.log("InputFields", inputFields);
  };

  const handleChangeInput = (id, event) => {
    const newInputFields = inputFields.map((i) => {
      if (id === i.id) {
        i[event.target.name] = event.target.value;
      }
      return i;
    });

    setInputFields(newInputFields);
    if (inputFields[inputFields.length - 1].id === id) {
      setInputFields([
        ...inputFields,
        { id: uuidv4(), x1: "", y1: "", y2: "", y3: "", y4: "" },
      ]);
    }
  };

  // const handleAddFields = () => {
  //   setInputFields([...inputFields, { id: uuidv4(),  x1: "", y1: "" , y2: "", y3: "", y4: "" }])
  // }

  const handleRemoveFields = (id) => {
    const values = [...inputFields];
    values.splice(
      values.findIndex((value) => value.id === id),
      1
    );
    setInputFields(values);
  };

  return (
    <div>
      <h1>MultiAxis Graph</h1>
      <label >Column:</label>

      <select onChange={(e)=>{setColumn(e.target.value)}}>
      <option value={1}> 1</option>
  <option value={2} > 2</option>
  <option value={3}> 3</option>
  <option value={4}> 4</option>
</select>









      <table>
        <thead>
          <tr>
            <th>XAxis</th>
            <th>YAxis1</th>
            {column >= 2 && <th>YAxis2</th>}
            {column >= 3 && <th>YAxis3</th>}
              {column >= 4 && <th>YAxis4</th>}
            <th>Remove cell</th>
            {/* <th>Add Cell</th> */}
          </tr>
        </thead>
        <tbody>
          {inputFields.map((inputField) => (
            <tr key={inputField.id}>
              <td>
                <input
                  name="x1"
                  style={{ width: "100px" }}
                  value={inputField.x}
                  onChange={(event) => handleChangeInput(inputField.id, event)}
                />
              </td>

              <td>
                <input
                  name="y1"
                  style={{ width: "100px" }}
                  value={inputField.y1}
                  onChange={(event) => handleChangeInput(inputField.id, event)}
                />
              </td>
{column >= 2 &&
              <td>
                <input
                  name="y2"
                  style={{ width: "100px" }}
                  value={inputField.y2}
                  onChange={(event) => handleChangeInput(inputField.id, event)}
                />
              </td>
}
{column >=3 &&
              <td>
                <input
                  name="y3"
                  style={{ width: "100px" }}
                  value={inputField.y3}
                  onChange={(event) => handleChangeInput(inputField.id, event)}
                />
              </td>
}
{column >= 4 &&
              <td>
                <input
                  name="y4"
                  style={{ width: "100px" }}
                  value={inputField.y4}
                  onChange={(event) => handleChangeInput(inputField.id, event)}
                />
              </td>
}
              <td>
                <button
                  disabled={inputFields.length === 1}
                  onClick={() => handleRemoveFields(inputField.id)}
                >
                  remove
                </button>
              </td>
          
            </tr>
          ))}
        </tbody>
      </table>

      <br/>


<Button
variant='contained'
  onClick={()=>generate()}
>Generate</Button>

<br/>

      <br />

      <div>
        {/* <LineChart width={600} height={300} data={data}>
    <Line  dataKey="y1" stroke="#8884d8" />
    <CartesianGrid stroke="#ccc" />
    <XAxis dataKey="x1" />
    <YAxis />
  </LineChart>    */}
        {temp && (
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

              <YAxis yAxisId="right1" orientation="left"  dataKey="y1" domain={[0, maxval1]} />
              {column >=2 &&        <YAxis yAxisId="right2" orientation="left"  dataKey="y2" domain={[0, maxval2]} />}
          {column >=3 &&        <YAxis yAxisId="right3" orientation="left"  dataKey="y3"  domain={[0, maxval3]}/>}
          {column >=4 &&        <YAxis yAxisId="right4" orientation="left"  dataKey="y4"  domain={[0, maxval4]}/>}
          
              <Tooltip />
              <Legend />
              <Line
              yAxisId="right1"
                type="monotone"
                dataKey="y1"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
              />
  {column >=2 &&            <Line
  yAxisId="right2"
                type="monotone"
                dataKey="y2"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
              />
  }
        {column >=3 &&      <Line
        yAxisId="right3"
                type="monotone"
                dataKey="y3"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
              />
        }
         {column >=4 &&     <Line
         yAxisId="right4"
                type="monotone"
                dataKey="y4"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
              />
         }
      

            </LineChart>
          </ResponsiveContainer>
        )}
      </div>
    </div>
  );
}

export default Multiaxis;
