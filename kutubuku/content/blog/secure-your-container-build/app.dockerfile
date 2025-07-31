FROM alpine

ARG API_URL
ARG API_TOKEN

RUN echo "API_URL=${API_URL}" > /config.txt
RUN echo "API_TOKEN=${API_TOKEN}" > /token.txt

# docker build \
#     -f app.dockerfile \
#     --build-arg API_URL=https://api.example.com \
#     --build-arg API_TOKEN=super_secret_12345 \
#     -t app .
