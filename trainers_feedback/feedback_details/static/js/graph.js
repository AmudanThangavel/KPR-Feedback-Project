// Get the canvas element
var canvas = document.getElementById("graph");
// Set the data for the graph
var data = {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [{
        label: "Sales",
        data: [2, 1, 3, 5, 4, 3],
        backgroundColor: "rgba(75,192,192,0.4)",
        borderColor: "rgba(75,192,192,1)"
    }]
};



// Set the options for the graph
var options = {
    scales: {
        y: {
            beginAtZero: true,
            ticks: {
                min: 0,
                max: 5,
                stepSize: 1,
                callback: function (value, index, values) {
                    if (Math.floor(value) === value) {
                        return value;
                    }
                }
            }
        }
    }
};

// Create the bar chart
var barChart = new Chart(canvas, {
    type: 'bar',  //change the type to bar
    data: data,
    options: options
});
