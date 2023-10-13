#camel <- function(x){ #function for camel case
#      str_to_title((paste(unlist(str_split(x, '_')), collapse=' '))) 
#}


camel <- function(x) {
  words <- unlist(str_split(x, '_'))
  new_words <- str_to_title(paste(words, collapse = ' '))
}

round_df <- function(df, digits) {
  nums <- vapply(df, is.numeric, FUN.VALUE = logical(1))

  df[,nums] <- round(df[,nums], digits = digits)

  return(df)
}

highlight_text <- function(x, color,weight="normal",type="normal") {
  sprintf("<span style='color: %s;font-weight: %s;font-style: %s;'>%s</span>", color,weight,type,x)
}

get_unique_keys <- function(data) {#function to get unique keys from the data in yaml dict
    unique_keys <- unique(gsub("\\..*","",colnames(as.data.frame(data))))
    return(unique_keys)
}

