import { connect, AmqpConnectOptions } from "jsr:@nashaddams/amqp";

const QUEUE_NAME = "sensor_data";

const connectionOptions: AmqpConnectOptions = {
  hostname: Deno.env.get("RABBITMQ_HOST") || "localhost",
  port: Number(Deno.env.get("RABBITMQ_PORT")) || 5672,
  username: Deno.env.get("RABBITMQ_USERNAME") || "guest",
  password: Deno.env.get("RABBITMQ_PASSWORD") || "guest",
}

const sockets = new Set<WebSocket>();

Deno.serve({ port: 8080 }, (req) => {
  const { socket, response } = Deno.upgradeWebSocket(req);
  socket.onopen = () => {
    console.log("🐇 WebSocket client connected");
    sockets.add(socket);
  };
  socket.onclose = () => sockets.delete(socket);
  socket.onerror = () => sockets.delete(socket);
  return response;
});

async function main() {
  const connection = await connect(connectionOptions);
  const channel = await connection.openChannel();

  await channel.declareQueue({ queue: QUEUE_NAME });
  await channel.consume(
    { queue: QUEUE_NAME },
    async (args, _, data) => {
      const message = new TextDecoder().decode(data);
      console.log("🐇 Received:", message);

      for (const socket of sockets) {
        try {
          socket.send(message);
        } catch (_) {
          sockets.delete(socket);
        }
      }

      await channel.ack({ deliveryTag: args.deliveryTag });
    },
  );
}

main();