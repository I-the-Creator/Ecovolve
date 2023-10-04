#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_DATA_POINTS 10

// Function to plot data using Gnuplot
void plotData(FILE *gnuplotPipe, int dataPoints[], int numPoints) {
  fprintf(
      gnuplotPipe,
      "plot '-' with filledcurves x1\n"); // Fill between the curve and x1 axis
  for (int i = 0; i < numPoints; i++) {
    fprintf(gnuplotPipe, "%d\n", dataPoints[i]); // Send data point
  }
  fprintf(gnuplotPipe, "e\n"); // End of data
  fflush(gnuplotPipe);         // Flush the pipe to update the plot
}

int main() {
  FILE *gnuplotPipe = popen("gnuplot -persist", "w"); // Open Gnuplot pipe
  if (!gnuplotPipe) {
    fprintf(stderr, "Error opening Gnuplot pipe\n");
    return 1;
  }

  int dataPoints[MAX_DATA_POINTS];
  int numPoints = 0;

  while (1) {
    // Generate random data (replace this with your data source)
    int newData = rand() % 100;

    // Add new data point to the array
    dataPoints[numPoints] = newData;
    numPoints++;

    if (numPoints > MAX_DATA_POINTS) {
      // Remove the oldest data point to keep a sliding window of data
      for (int i = 0; i < MAX_DATA_POINTS - 1; i++) {
        dataPoints[i] = dataPoints[i + 1];
      }
      numPoints = MAX_DATA_POINTS - 1;
    }

    // Plot the updated data
    plotData(gnuplotPipe, dataPoints, numPoints);

    // Sleep to control the update rate (adjust as needed)
    usleep(100000); // Sleep for 0.1 seconds
  }

  // Close the Gnuplot pipe
  pclose(gnuplotPipe);

  return 0;
}
