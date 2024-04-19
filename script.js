const makeAxiosCall = async (endpoint) => {
  const getDataUrl = `http://127.0.0.1:5000/${endpoint}`;
  const res = await axios.get(getDataUrl);
  
  switch (endpoint) {
    case "task1": 

      const labels = res.data.map(item => item.count);
      const values = res.data.map(item => item.averageValueForMoney);

      const retval = 
        {
            labels: labels,
            datasets: [{
                label: 'Average Value for Money',
                data: values,
                borderColor: 'rgb(75, 192, 192)',
                borderWidth: 1
            }]
        };

      return retval

    case "task2":
      const sentimentAnalysis = res.data[0].sentimentAnalysis;

      // Define a new variable specific for Task 2 to avoid conflicts
      const sentimentCountsTask2 = {
        negative: sentimentAnalysis.negative,
        neutral: sentimentAnalysis.neutral,
        positive: sentimentAnalysis.positive
      };
    
      console.log('Task 2 Sentiment Counts:', sentimentCountsTask2);
    
      // Prepare the data for the bar chart
      const dataForTask2Chart = {
        labels: ['Negative', 'Neutral', 'Positive'],
        datasets: [{
          label: 'Sentiment Analysis on "Value for Money" ',
          data: [
            sentimentCountsTask2.negative,
            sentimentCountsTask2.neutral,
            sentimentCountsTask2.positive
          ],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(75, 192, 192, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(75, 192, 192, 1)'
          ],
          borderWidth: 1
        }]
      };
    
      console.log('Task 2 Chart Data:', dataForTask2Chart);
      return dataForTask2Chart;
      
    case "task3":
      const sentimentCounts = {
        negative: 0,
        neutral: 0,
        positive: 0
    };
  

    res.data.forEach(entry => {
        entry.sentiments.forEach(sentiment => {
            sentimentCounts[sentiment.toLowerCase()]++;
        });
    });


    console.log(sentimentCounts)
      const data = {
        labels: ['Negative', 'Neutral', 'Positive'],
        datasets: [{
            label: 'Sentiment Analysis on Route Popularity',
            data: [
                sentimentCounts.negative,
                sentimentCounts.neutral,
                sentimentCounts.positive
            ],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    };

    console.log(data)
      return data
    default:
      break;
  }


};

const mainFunc = async () => {
  const ctxQuery1 = document.getElementById("chartQuery1").getContext("2d");
  new Chart(ctxQuery1, {
    type: 'line',
    data: await makeAxiosCall("task1")
  });

  const ctxQuery2 = document.getElementById("chartQuery2").getContext("2d");
  new Chart(ctxQuery2, {
    type: "bar",
    data: await makeAxiosCall("task2")
  });

  const ctxQuery3 = document.getElementById("chartQuery3").getContext("2d");
  new Chart(ctxQuery3, {
    type: "bar",
    data: await makeAxiosCall("task3")
  });
}

["hashchange", "load"].forEach(event => {
  window.addEventListener(event, mainFunc);
});