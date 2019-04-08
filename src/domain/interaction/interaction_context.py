from src.domain.interaction.receiving_question_interaction_state import ReceivingQuestionInteractionState
from src.domain.interaction.receiving_statement_context_interaction_state import \
    ReceivingStatementContextInteractionState


class InteractionContext:
    SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE = "I have no more questions to ask"
    SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE = "I am ready to ask questions"

    def __init__(self, interaction_state):
        self.interaction_state = interaction_state

    def fetch_next_interaction_state(self, input_text):
        next_interaction_state = self.interaction_state
        if input_text == self.SWITCHING_TO_STATEMENT_CONTEXT_PHASE_MESSAGE:
            next_interaction_state = ReceivingStatementContextInteractionState()
        elif input_text == self.SWITCHING_TO_QUESTION_ANSWERING_PHASE_MESSAGE:
            next_interaction_state = ReceivingQuestionInteractionState()
        return next_interaction_state
