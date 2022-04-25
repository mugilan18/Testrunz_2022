import { useEffect } from "react";
import React from "react";
import CanvasJSReact from "../assets/canvasjs.react";

const Linechart = () => {
  var CanvasJSChart = CanvasJSReact.CanvasJSChart;

  var x1 = [2, 6, 10, 12, 16, 20];
  var y1 = [70, 69, 68, 67, 66, 65];
  var dataPoints = [];
  	useEffect(()=>{
		for (var i = 0; i < 6; i++) {
			dataPoints.push({
			  x: x1[i],
			  y: y1[i]
			});
		  }
	},[])
    		const options = {
animationEnabled: true,
			
			title:{
				text: "Lee's Disc method"
			},
			axisX:
		{
			title: "Time sec",
		},
			axisY:{
				title: "Temperature ‘c",
				includeZero: false,
			
			},
			data: [{
				type: "line",
				dataPoints: dataPoints
	
			}]
		}
  return (
  <div>
	  <CanvasJSChart options = {options} /> </div>
  );
};

export default Linechart;
