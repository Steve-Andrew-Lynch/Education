complete <- function(directory, id = 1:332) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'id' is an integer vector indicating the monitor ID numbers
  ## to be used
  
  ## Return a data frame of the form:
  ## id nobs
  ## 1  117
  ## 2  1041
  ## ...
  ## where 'id' is the monitor ID number and 'nobs' is the
  ## number of complete cases
  nobs <- numeric()
  
  source("getmonitor.R") 
  
  source("getmonitor.R")
  
  nobs <- numeric()
  
  for ( i in id ) { 
    data <- getmonitor(i, directory)  
    cc <- sum(complete.cases(data))
    nobs <- c(nobs, cc)
  }  
  
  return ( data.frame(id=id, nobs=nobs)  ) 
  
}

##complete("specdata", 1)
##complete("specdata", 2)
##complete("specdata", 30:25)

source("http://spark-public.s3.amazonaws.com/compdata/scripts/complete-test.R")
complete.testscript()