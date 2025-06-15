FROM ruby:3.1

# Instala dependencias necesarias
RUN apt-get update -qq && \
    apt-get install -y build-essential curl nodejs npm

# Instala Yarn con NPM directamente
RUN npm install -g yarn

# Directorio del sitio
WORKDIR /site

# Copia el Gemfile y lo instala
COPY Gemfile* ./
RUN bundle install

# Copia el resto del contenido
COPY . .

EXPOSE 4000

# Ejecuta Jekyll
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]