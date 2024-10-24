# Usar una imagen base oficial de Ruby
FROM ruby:3.0

# Instalar las dependencias necesarias para construir gemas nativas y Jekyll
RUN apt-get update -qq && apt-get install -y build-essential

# (Opcional) Instalar Node.js para soporte de JavaScript y Yarn para manejo de paquetes
RUN curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g yarn

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /site

# Añadir el Gemfile y Gemfile.lock al directorio de trabajo
COPY Gemfile* /site/

# Actualizar RubyGems y Bundler
RUN gem update --system 3.2.22 && gem install bundler

# Instalar las gemas, incluyendo Jekyll
RUN bundle install

# Copiar el resto del proyecto Jekyll al contenedor
COPY . /site

# Exponer el puerto 4000 para el servidor Jekyll
EXPOSE 4000

# Comando para iniciar Jekyll en modo servidor
CMD ["jekyll", "serve", "--host", "0.0.0.0"]
