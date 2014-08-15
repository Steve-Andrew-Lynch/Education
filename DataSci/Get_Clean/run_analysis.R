## Goals
## 1. Create a tidy data set with each variable should be in one column
## 2. Ensure that each observation of that variable should be in a diferent row
## 3. include activities to link tables together in one data table

## Merges the training and the test sets to create one data set.

install.packages("stringr", dependencies = TRUE)
install.packages("reshape2")
library("stringr")

setwd("Education/DataSci/Get_Clean") 
train_test <- data.frame() #Great a blank data frame, this will be the final cleaned data set
cleaned_data <- data.frame() #Another blank data frame, for the final tidy data set

activity_labels <- c("WALKING", "WALKING_UPSTAIRS", "WALKING_DOWNSTAIRS", "SITTING", "STANDING", "LAYING")

# Read in the test data set and then add it to a new list called test_clean
test_text <- scan("UCI HAR Dataset/test/X_test.txt", character(0), sep="\n")
test_clean <- list()
for (i in test_text) {
  x <- str_trim(unlist(i))
  x <- strsplit(x, "[ ]{1,}")
  x <- lapply(x, as.numeric)
  test_clean <- c(test_clean, x)
}
# Read in the training data set and then add it to a new list called train_clean
train_text <- scan("UCI HAR Dataset/train/X_train.txt", character(0), sep="\n")
train_clean <- list()
for (i in train_text) {
  x <- str_trim(unlist(i))
  x <- strsplit(x, "[ ]{1,}")
  x <- lapply(x, as.numeric)
  train_clean <- c(test_clean, x)
}

#Add the training and test data sets together, calculate SD and mean
train_test_raw <- c(train_clean, test_clean)
train_test_mean <- list()
train_test_sd <- list()

#calculate the SD, save it to the list
for (i in train_test_raw) {
  train_test_sd <- c(train_test_sd, sd(unlist(i)))
  
}
train_test_sd <- unlist(train_test_sd)

#calculate the mean, save it to the list
for (i in train_test_raw) {
  train_test_mean <- c(train_test_mean, mean(unlist(i)))
  
}
train_test_mean <- unlist(train_test_mean)

# Read in a list for y_values (actvity values), add them to a single list called "y"
ytrain <- readLines("UCI HAR Dataset/train/y_train.txt")
ytest <- readLines("UCI HAR Dataset/test/y_test.txt")
y_vals <- c(ytrain, ytest)
y <- list()

for (i in y_vals) {
  if (i == "1") {
    y <- c(y, "WALKING")
  } else if (i == "2"){
    y <- c(y, "WALKING_UPSTAIRS")
  } else if (i == "3"){
    y <- c(y, "WALKING_DOWNSTAIRS")
  } else if (i == "4"){
    y <- c(y, "SITTING")
  } else if (i == "5"){
    y <- c(y, "STANDING")
  } else if (i == "6"){
    y <- c(y, "LAYING")
  }
}

# Read in the test & train subject names and then add them into a single list
test_subject <- readLines("UCI HAR Dataset/test/subject_test.txt")
train_subject <- readLines("UCI HAR Dataset/train/subject_train.txt")
sub_vals <- c(train_subject, test_subject)

train_test <- cbind("Subject" = as.numeric(sub_vals), "Activity"= as.character(y), "SD" = as.numeric(train_test_sd), "Mean" = as.numeric(train_test_mean))
#separates data for tidy data set

#final clean data set
cleaned_data <- as.data.frame(train_test, stringsAsFactors = FALSE)

#print this 

library("reshape2")

id_vars = c("Subject", "Activity")
melted1 <- melt(cleaned_data, id=id_vars, "Mean", value.name="Mean")
melted2 <- melt(cleaned_data, id=id_vars, "SD", value.)
dcast(melted1, Subject ~ Activity + value)  

# #tidying data set
# cleaned_data[,1] <- as.numeric(cleaned_data[,1])
# 
# for (i in cleaned_data[,1]) {
#   for (x in activity_labels) {
#     
#   }
# }
# 
# cleaned_data[,1] ==1
# 
