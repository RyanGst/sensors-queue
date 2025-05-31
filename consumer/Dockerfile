FROM denoland/deno:2.3.5

WORKDIR /app

COPY . .

RUN deno cache main.ts

EXPOSE 8080
# Run the apps
CMD ["deno", "run", "--allow-net", "--allow-env", "main.ts"]