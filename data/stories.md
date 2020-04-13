## Some question from FAQ
* faq
    - respond_faq
    - action_restart

## covid form
* ask_covid
    - covid_form
    - form{"name": "covid_form"}
    - form{"name": null}
    - action_restart

## covid form with country included
* ask_covid{"country":"Ireland"}
    - covid_form
    - form{"name": "covid_form"}
    - form{"name": null}
    - action_restart

## out of scope
* out_of_scope
    - utter_out_of_scope
    - action_restart
