FROM alpine

ARG API_URL

RUN echo "API_URL=${API_URL}" > /config.txt
RUN --mount=type=secret,id=api_token \
    cat /run/secrets/api_token > /token.txt

# docker build \
#     -f secure-app.dockerfile \
#     --build-arg API_URL=https://api.example.com \
#     --secret id=api_token,env=API_TOKEN \
#     -t secure-app .
