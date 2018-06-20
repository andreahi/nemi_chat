## greet
* greet
    - utter_greet

## thank
* thank
    - utter_thank

## bye
* bye
    - utter_bye


## change subscription
* change_subscription
- utter_change_subscription
> buy specific subscription

## specify change subscription yng
> buy specific subscription
* confirm_change_subscription_yng
- ack_change_subscription_yng  
 
## confused change subscription yng
* confirm_change_subscription_yng
- utter_repeat_question 
    
## specify change subscription medium
> buy specific subscription
* confirm_change_subscription_medium
- ack_change_subscription_medium    
    
## confused change subscription medium
* confirm_change_subscription_medium
- utter_repeat_question 

## specify change subscription flexi
> buy specific subscription
* confirm_change_subscription_flexi
- ack_change_subscription_flexi   
  
## confused change subscription flexi
* confirm_change_subscription_flexi
- utter_repeat_question 
     

## change subscription yng
* change_subscription_yng
- ack_change_subscription_yng  
    
## change subscription medium
* change_subscription_medium
- ack_change_subscription_medium    

## change subscription flexi
* change_subscription_flexi
- ack_change_subscription_flexi   
     

     

## change subscription yng
* change_subscription_yng
- ack_change_subscription_yng  
    
## change subscription medium
* change_subscription_medium
- ack_change_subscription_medium    

## change subscription flexi
* change_subscription_flexi
- ack_change_subscription_flexi   
     

     
## get puk
* get_puk
- utter_get_puk
* affirm
- ack_get_puk


## need data
* trenger_data
- utter_buy_data
> buy_spesific_data_amount

## confirm data 1
> buy_spesific_data_amount
* confirm_buy_1gb
- ack_buy_data_1gb
    
#confused confirm_buy_1gb
* confirm_buy_1gb
- utter_repeat_question

## confirm data 5
> buy_spesific_data_amount
* confirm_buy_5gb
- ack_buy_data_5gb  

#confused confirm data 5
* confirm_buy_5gb
- utter_repeat_question 
     
## confirm data 10
> buy_spesific_data_amount
* confirm_buy_10gb
- ack_buy_data_10gb

#confused confirm data 10
* confirm_buy_10gb
- utter_repeat_question 
     

## data 1
* buy_1gb
- ack_buy_data_1gb
    
## data 5
* buy_5gb
- ack_buy_data_5gb   
     
## data 10
* buy_10gb
- ack_buy_data_10gb
    
    
## get invoices
* get_invoice_page
- utter_get_invoice_page

## get data usage
* get_data_usage
- utter_get_data_usage

## get data usage msisdn
* get_data_usage_msisdn
- utter_get_data_usage_msisdn

## get swap info
* get_swap_info
- utter_get_swap_info


# random sentences
* random
- utter_random