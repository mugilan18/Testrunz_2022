import React,{useState} from 'react'
import Multiaxis from './Multiaxis'
import Multichart from './Multichart'
import Singleaxis from './Singleaxis'

const Graph = () => {
  const[graphtype,setGraphtype]=useState("simple")
  return (
    <div>
    <select onChange={(e)=>{setGraphtype(e.target.value)}}>
  <option value={"simple"} > Simple Graph</option>
  <option value={"multichart"}> Multi Chart Graph</option>
  <option value={"multiaxis"}> Multi axis Graph</option>
</select>
 {graphtype==="simple"   && <div><Singleaxis/></div>}
 {graphtype==="multichart"  && <div><Multichart/></div>}
 {graphtype==="multiaxis"  && <div><Multiaxis/></div>}

    </div>
  )
}

export default Graph