import React from "react";
import CanvasJSReact from '../canvasjs-2.3.2/Chart 2.3.2 GA - Stable/canvasjs.react.js';
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
class Result extends React.Component{
    constructor(props){
	  super(props);
	  this.state={
	  	data:this.props.res
	  }
	  
    }
   
   render(){
	  var dataset=[]
	  var data=this.state.data
	   for (var key in data){
		dataset.push({y : data[key] , label : key})
	  }
	  console.log(dataset[0]);
	const options = {
		animationEnabled: true,
		theme: "dark",
		title:{
			text: "Model Interpretation"
		},
		axisX: {
			
			reversed: true,
		},
		
		data: [{
			type: "bar",
			dataPoints: [
				dataset[0],
				dataset[1],
				dataset[2],
				dataset[3],
				dataset[4],
				dataset[5],
				dataset[6],
				dataset[7],
				dataset[8],
				dataset[9],
				dataset[10],
				dataset[11]
			]
		}]
	}
	return (
	<div>
		<p>The predicted price for the car is <strong>{this.state.data.res} Lakh Rupees</strong> </p>
		<CanvasJSChart options = {options}
			/* onRef={ref => this.chart = ref} */
		/>
		<br></br>
		<p className="container">
			This will tell how each feature is effecting the final result (positively or negetively)<br></br>
			The Score will tell for how much extent its effecting<br></br>
		</p>
		{/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
	</div>
	);
}

   

}
export default Result;