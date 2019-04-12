from src.domain.interaction.exit_phase import ExitPhase
from src.domain.interaction.interaction_phase_state import InteractionPhaseState


class QuestionAnsweringPhase(InteractionPhaseState):

    SWITCHING_TO_EXIT_PHASE_MESSAGE = "I have no more questions to ask."

    def fetch_next_interaction_phase(self, input_text):
        if input_text == self.SWITCHING_TO_EXIT_PHASE_MESSAGE:
            return ExitPhase()
        return self

    def process_input_text(self, input_text, input_text_processor):
        return input_text_processor.process_question(input_text)