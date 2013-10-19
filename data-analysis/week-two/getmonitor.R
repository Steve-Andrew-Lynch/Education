getmonitor <- function(id, directory, summarize = FALSE) {
  ## 'id' is a vector of length 1 indicating the monitor ID
  ## number. The user can specify 'id' as either an integer, a
  ## character, or a numeric.
  
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'summarize' is a logical indicating whether a summary of
  ## the data should be printed to the console; the default is
  ## FALSE
  
  id <- as.integer(id) 
  
  if (id < 10) {
    file_name <- paste(directory, "/", "00", id, ".csv", sep="")
  } else if (id < 100 ) {
    file_name <- paste(directory, "/", "0", id, ".csv", sep="")
  } else {
    file_name <- paste(directory, "/", id, ".csv", sep="")
  }
  
  data <- read.csv(file_name)
  
  if ( summarize ) {
    print(summary(data))
  }
  return (data)
}

##data <- getmonitor(1, "specdata", TRUE)
##head(data)
##data <- getmonitor(101, "specdata", TRUE)
##head(data)
##data <- getmonitor(200, "specdata", TRUE)