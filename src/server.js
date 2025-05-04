const fastify = require("fastify")({ logger: true });
const { fastifyCors } = require("@fastify/cors");
const port = process.env.PORT

fastify.register(fastifyCors, { origin: process.env.AUTH_ADDR })
fastify.register(require("./routes"), { prefix: "/" })

fastify.listen({ port }, (err, address) => {
    if (err) {
        fastify.log.error(err)
        process.exit(1)
    }

    console.log(`running on port: ${port}`)
})
