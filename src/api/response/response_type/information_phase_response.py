from src.api.response.response import Response
from src.api.response.response_tag import ResponseTag


class InformationPhaseResponse(Response):

    def print(self):
        print(
            "\n" + ResponseTag.GATHER_INFORMATION_TAG.__str__().format(self.output) + "\n" +
            ResponseTag.ENTER_INFORMATION_TAG.__str__() + "\n"
        )
