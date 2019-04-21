from sensitivity import test
from post import plot
from core import clean, log

#   This method cleans the remnant files from the last run
clean()

#   Here, we define the parameters and values to investiate
test_params = [{'epoch':[50,100]}, {'latent':[20,30]}]

#   Perform sensitivity analysis
test(test_params)

#   Getting the plots saved in the temp folder
plot(test_params)