#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>
#define buf_size 5

sem_t sem_empty;
sem_t sem_full;
pthread_mutex_t mutex;

int buffer[buf_size];
int prod_idx = 0;
int cons_idx = 0;

void* producer(void *idx) {
    int i = (long int)idx;
    while (true) {
        int num = rand() % 100;
        printf("Producer no.%d produced: %d\n", i, num);
        sleep(rand() % 4);
        sem_wait(&sem_empty);
        pthread_mutex_lock(&mutex);
        buffer[prod_idx] = num;
        prod_idx++;
        prod_idx = (prod_idx + 1) % buf_size;
        pthread_mutex_unlock(&mutex);
        sem_post(&sem_full);
    }
}

void* consumer(void *idx) {
    int i = (long int)idx;
    while (true) {
        sem_wait(&sem_full);
        pthread_mutex_lock(&mutex);
        int num = buffer[cons_idx];
        cons_idx++;
        printf("Consumer no.%d consumed: %d\n", i, num);
        cons_idx = (cons_idx + 1) % buf_size;
        pthread_mutex_unlock(&mutex);
        sem_post(&sem_empty);
        sleep(rand() % 4);
    }
}

int main() {
    srand(time(0));
    int num_prod, num_cons;
    printf("Enter the number of Producers: ");
    scanf("%d", &num_prod);
    printf("Enter the number of Consumers: ");
    scanf("%d", &num_cons);

    pthread_t prod[num_prod], cons[num_cons];
    pthread_mutex_init(&mutex, NULL);
    sem_init(&sem_empty, 0, buf_size);
    sem_init(&sem_full, 0, 0);

    for (long int idx = 0; idx < num_prod; idx++) {
        pthread_create(&prod[idx], NULL, &producer, (void *)idx);
    }
    for (long int idx = 0; idx < num_cons; idx++) {
        pthread_create(&cons[idx], NULL, &consumer, (void *)idx);
    }

    for (int idx = 0; idx < num_prod; idx++) {
        pthread_join(prod[idx], NULL);
    }
    for (int idx = 0; idx < num_cons; idx++) {
        pthread_join(prod[idx], NULL);
    }

    sem_destroy(&sem_empty);
    sem_destroy(&sem_full);
    pthread_mutex_destroy(&mutex);

    return 0;
}

