corr <- function(directory, threshold = 0) {
  ## 'directory' is a character vector of length 1 indicating
  ## the location of the CSV files
  
  ## 'threshold' is a numeric vector of length 1 indicating the
  ## number of completely observed observations (on all
  ## variables) required to compute the correlation between
  ## nitrate and sulfate; the default is 0
  
  ## Return a numeric vector of correlations

  source("getmonitor.R")
  
  id <- 1:332
  
  my_func <- function(x) { 
    
    v <- getmonitor(x, directory)
    
    if ( sum(complete.cases(v) ) > threshold ) {
      my_answer <- cor(v$sulfate, v$nitrate, "complete.obs")
      return ( my_answer )
    } else {
      return ( NA )
    }
  }
  
  # sapply extracts one item at a time from id 
  # and gives that item to my_func 
  # its sort of like an auotmatic loop 
  # then sapply returns a vector containing the cor values or NA 
  
  ret_val <- sapply(id, my_func)
  
  # strip out the NAs 
  # but what happens if they are ALL NAs and we strip out everything ?
  # that's ok, just return an empty numeric vector 

  return ( as.numeric( ret_val[!is.na(ret_val)] ) )

}

##cr<-corr("specdata", 150)
##head(cr)
##summary(cr)
##cr<-corr("specdata", 400)
##head(cr)