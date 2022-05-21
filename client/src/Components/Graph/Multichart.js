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
function Multichart() {
  const [inputFields, setInputFields] = useState([
    { id: uuidv4(),x1: "", x2: "", x3: "", x4: "", x5: "", x6: "", x7: "", x8: "", y1: "", y2: "", y3: "", y4: "", y5: "", y6: "", y7: "", y8: "" },
  ]);
  const [maxval1, setMaxval1] = useState();
  const [maxval2, setMaxval2] = useState();
  const [maxval3, setMaxval3] = useState();
  const [maxval4, setMaxval4] = useState();
  const [maxval5, setMaxval5] = useState();
  const [maxval6, setMaxval6] = useState();
  const [maxval7, setMaxval7] = useState();
  const [maxval8, setMaxval8] = useState();

  const [temp, setTemp] = useState();
  const [column, setColumn] = useState();
  const [data, setData] = useState();

  const generate = () => {
    setTemp();
    let yval1 = inputFields.map((obj) => obj.y1);
    let yval2 = inputFields.map((obj) => obj.y2);
    let yval3 = inputFields.map((obj) => obj.y3);
    let yval4 = inputFields.map((obj) => obj.y4);
    let yval5 = inputFields.map((obj) => obj.y5);
    let yval6 = inputFields.map((obj) => obj.y6);
    let yval7 = inputFields.map((obj) => obj.y7);
    let yval8 = inputFields.map((obj) => obj.y8);

    let newyval1 = yval1.map(Number);
    let newyval2 = yval2.map(Number);
    let newyval3 = yval3.map(Number);
    let newyval4 = yval4.map(Number);
    let newyval5 = yval5.map(Number);
    let newyval6 = yval6.map(Number);
    let newyval7 = yval7.map(Number);
    let newyval8 = yval8.map(Number);

    // let ylist = [...newyval1,...newyval2,...newyval3,...newyval4]
    setMaxval1(Math.max(...newyval1));
    setMaxval2(Math.max(...newyval2));
    setMaxval3(Math.max(...newyval3));
    setMaxval4(Math.max(...newyval4));
    setMaxval5(Math.max(...newyval5));
    setMaxval6(Math.max(...newyval6));
    setMaxval7(Math.max(...newyval7));
    setMaxval8(Math.max(...newyval8));
    // let tempinputFields = inputFields.splice(-1);
    // setInputFields(tempinputFields)
    setTemp(inputFields);
    setData(inputFields)
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
        { id: uuidv4(), x1: "", x2: "", x3: "", x4: "", x5: "", x6: "", x7: "", x8: "", y1: "", y2: "", y3: "", y4: "", y5: "", y6: "", y7: "", y8: "" },
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
      <h1>Multi Graph</h1>
      <label>Column:</label>

      <select
        onChange={(e) => {
          setColumn(e.target.value);
        }}
      >
        <option value={1}> 1</option>
        <option value={2}> 2</option>
        <option value={3}> 3</option>
        <option value={4}> 4</option>
        <option value={5}> 5</option>
        <option value={6}> 6</option>
        <option value={7}> 7</option>
        <option value={8}> 8</option>
      </select>
      <table>
        <thead>
          <tr>
            <th>XAxis1</th>
            <th>YAxis1</th>

            {column >= 2 && <th>XAxis2</th>}
            {column >= 2 && <th>YAxis2</th>}

            {column >= 3 && <th>XAxis3</th>}
            {column >= 3 && <th>YAxis3</th>}

            {column >= 4 && <th>XAxis4</th>}
            {column >= 4 && <th>YAxis4</th>}

            {column >= 5 && <th>XAxis5</th>}
            {column >= 5 && <th>YAxis5</th>}

            {column >= 6 && <th>XAxis6</th>}
            {column >= 6 && <th>YAxis6</th>}

            {column >= 7 && <th>XAxis7</th>}
            {column >= 7 && <th>YAxis7</th>}

            {column >= 8 && <th>XAxis8</th>}
            {column >= 8 && <th>YAxis8</th>}

            <th>Remove cell</th>
        
          </tr>
        </thead>
        <tbody>
          {inputFields.map((inputField) => (
            <tr key={inputField.id}>
              <td>
                <input
                  name="x1"
                  style={{ width: "100px" }}
                  value={inputField.x1}
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
              {column >= 2 && (
                <>
                  <td>
                    <input
                      name="x2"
                      style={{ width: "100px" }}
                      value={inputField.x2}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y2"
                      style={{ width: "100px" }}
                      value={inputField.y2}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}
              {column >= 3 && (
                <>
                  <td>
                    <input
                      name="x3"
                      style={{ width: "100px" }}
                      value={inputField.x3}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y3"
                      style={{ width: "100px" }}
                      value={inputField.y3}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}
              {column >= 4 && (
                <>
                  <td>
                    <input
                      name="x4"
                      style={{ width: "100px" }}
                      value={inputField.x4}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y4"
                      style={{ width: "100px" }}
                      value={inputField.y4}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}
              {column >= 5 && (
                <>
                  <td>
                    <input
                      name="x5"
                      style={{ width: "100px" }}
                      value={inputField.x5}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y5"
                      style={{ width: "100px" }}
                      value={inputField.y5}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}
              {column >= 6 && (
                <>
                  <td>
                    <input
                      name="x6"
                      style={{ width: "100px" }}
                      value={inputField.x6}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y6"
                      style={{ width: "100px" }}
                      value={inputField.y6}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}

              {column >= 7 && (
                <>
                  <td>
                    <input
                      name="x7"
                      style={{ width: "100px" }}
                      value={inputField.x7}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y7"
                      style={{ width: "100px" }}
                      value={inputField.y7}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}

              {column >= 8 && (
                <>
                  <td>
                    <input
                      name="x8"
                      style={{ width: "100px" }}
                      value={inputField.x8}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>

                  <td>
                    <input
                      name="y8"
                      style={{ width: "100px" }}
                      value={inputField.y8}
                      onChange={(event) =>
                        handleChangeInput(inputField.id, event)
                      }
                    />
                  </td>
                </>
              )}

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
      
        {temp && <>
             <ResponsiveContainer width="50%" aspect={2}>
            <LineChart
              width={500}
              height={300}
              data={data}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="x1" />
              <YAxis orientation="left" dataKey="y1" domain={[0, maxval1]} />
              <Tooltip />
              <Legend />
              <Line
                type="monotone"
                dataKey="y1"
                stroke="#8884d8"
                activeDot={{ r: 8 }}
              />
            </LineChart>
            </ResponsiveContainer>

            {column >= 2 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x2" />
                <YAxis orientation="left" dataKey="y2" domain={[0, maxval2]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y2"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}

            {column >= 3 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x3" />
                <YAxis orientation="left" dataKey="y3" domain={[0, maxval3]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y3"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}

            {column >= 4 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x4" />
                <YAxis orientation="left" dataKey="y4" domain={[0, maxval4]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y4"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}

            {column >= 5 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x5" />
                <YAxis orientation="left" dataKey="y5" domain={[0, maxval5]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y5"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}

            {column >= 6 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x6" />
                <YAxis orientation="left" dataKey="y6" domain={[0, maxval6]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y6"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}

            {column >= 7 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x7" />
                <YAxis orientation="left" dataKey="y7" domain={[0, maxval7]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y7"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}

            {column >= 8 && (
                <ResponsiveContainer width="50%" aspect={2}>
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                  top: 5,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="x8" />
                <YAxis orientation="left" dataKey="y8" domain={[0, maxval8]} />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="y8"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
              </ResponsiveContainer>
            )}
          </>
        }
      </div>
    </div>
  );
}

export default Multichart;
