import React from "react";
import Paper from "@material-ui/core/Paper";

import CanvasJSReact from "./canvasjs.react";
import visData from "./VisData";

const CanvasJSChart = CanvasJSReact.CanvasJSChart;

class Graph extends React.PureComponent {
  constructor(props) {
    super(props);

    this.state = {
      visD: {},
    };
    this.updateChart = this.updateChart.bind(this);
  }
  componentDidMount() {
    const remoteData = visData();
    remoteData.then((response) => {
      this.setState({ visD: response });
    });
    this.updateChart();
  }
  updateChart() {
    this.chart.render();
  }
  render() {
    const options = {
      animationEnabled: true,
      title: {
        text: this.state?.visD.title && this.state?.visD.title,
      },
      axisX: {
        title: this.state?.visD.XTitle && this.state?.visD.XTitle,
        valueFormatString: "###",
        suffix: "-(sec)",
      },
      axisY: {
        title: this.state?.visD.YTitle && this.state?.visD.YTitle,
        prefix: "O ",
        includeZero: false,
      },
      data: [
        {
          yValueFormatString: "O ###",
          xValueFormatString: "###",
          type: "spline",
          dataPoints: (this.state?.visD.resData &&
            this.state?.visD.resData.map((ele) => ele)) || [{ x: 0, y: 0 }],
        },
      ],
    };

    return (
      <Paper>
        <CanvasJSChart options={options} onRef={(ref) => (this.chart = ref)} />
      </Paper>
    );
  }
}

export default Graph;
