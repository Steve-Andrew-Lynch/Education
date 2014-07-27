## Goals
## 1. Create a tidy data set with each variable should be in one column
## 2. Ensure that each observation of that variable should be in a diferent row
## 3. include activities to link tables together in one data table

## Merges the training and the test sets to create one data set.

install.packages("stringr", dependencies = TRUE)
library("stringr")

train_test <- data.frame()

test_subject <- readLines("UCI HAR Dataset/test/subject_test.txt")
train_subject <- readLines("UCI HAR Dataset/train/subject_train.txt")
ytrain <- readLines("UCI HAR Dataset/train/y_train.txt")
ytest <- readLines("UCI HAR Dataset/test/y_test.txt")

test_text <- scan("UCI HAR Dataset/test/X_test.txt", character(0), sep="\n")
test_clean <- list()
for (i in test_text) {
  x <- str_trim(unlist(i))
  x <- strsplit(x, "[ ]{1,}")
  x <- lapply(x, as.numeric)
  test_clean <- c(test_clean, x)
}

train_text <- scan("UCI HAR Dataset/train/X_train.txt", character(0), sep="\n")
train_clean <- list()
for (i in train_text) {
  x <- str_trim(unlist(i))
  x <- strsplit(x, "[ ]{1,}")
  x <- lapply(x, as.numeric)
  train_clean <- c(test_clean, x)
}
train_clean

train_test_raw <- c(train_clean, test_clean)
train_test_vals <- list()




sub_vals <- c(train_subject, test_subject)
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

train_test <- cbind("Subject" <- sub_vals)
train_test <- cbind("Activity" <- y)



#test_act_dir <- "UCI HAR Dataset/test/Inertial Signals"
#train_act_dir <- "UCI HAR Dataset/train/Inertial Signals" 
#test_list <- dir(test_act_dir)
# train_list <- dir(train_act_dir)
# test_list
# train_list
# 
# makeTableData <- function(x, dir) {
#   x <- data.frame()
#   for (file in dir) {
#     x <- cbind(as.chraacter(i) <- readLines(paste(dir, file, sep = "/")))
#   }
#   
#   
# }