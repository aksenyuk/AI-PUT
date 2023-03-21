#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdbool.h>

#define no_prod 5
#define no_cons 6
#define buffer_size 10

struct buff
{
    int item_id[buffer_size];
    int next_in, next_out;
};

struct buff buffer;

pthread_t cons_id[no_cons], prod_id[no_prod];
sem_t empty, data;
pthread_mutex_t mutex;

int acquire_place_prod(long int id)
{
    int x;
    pthread_mutex_lock(&mutex);
    x = buffer.next_in;
    buffer.next_in = (buffer.next_in + 1) % buffer_size;
    printf("producer %ld will produce item at index %d\n", id, x);
    pthread_mutex_unlock(&mutex);
    return x;
}
int produce(long int id)
{
    sem_wait(&empty);
    int x = acquire_place_prod(id);
    sleep(rand() % 5);
    int item = rand() % 1000;
    buffer.item_id[x] = item;
    printf("producer %ld produced item %d\n", id, item);
    sem_post(&data);
    return 0;
}
void *producer(void *param)
{
    int item, i;
    int id = (long int)param;
    while (true)
    {
        produce(id);
    }
    pthread_exit(0);
}

int acquire_place_cons(long int id)
{
    int x;
    pthread_mutex_lock(&mutex);
    x = buffer.next_out;
    buffer.next_out = (buffer.next_out + 1) % buffer_size;
    printf("consumer %ld will consume item at index %d\n", id, x);
    pthread_mutex_unlock(&mutex);
    return x;
}

int consume(int *item, long int id)
{
    sem_wait(&data);
    int x = acquire_place_cons(id);
    while (buffer.item_id[x] == -1 || buffer.item_id[x] == 0)
        ;
    sleep(rand() % 5);
    *item = buffer.item_id[x];
    buffer.item_id[x] = -1;
    printf("consumer %ld consumed item %d\n", id, *item);
    sem_post(&empty);
    return 0;
}

void *consumer(void *param)
{
    int item;
    int id = (long int)param;
    while (true)
    {
        consume(&item, id);
    }
    pthread_exit(0);
}

int main()
{
    sem_init(&empty, 0, buffer_size);
    sem_init(&data, 0, 0);
    pthread_mutex_init(&mutex, NULL);
    for (long int i = 0; i < no_cons; i++)
    {
        pthread_create(&cons_id[i], NULL, consumer, (void *)i);
    }
    for (long int i = 0; i < no_prod; i++)
    {
        pthread_create(&prod_id[i], NULL, producer, (void *)i);
    }
    for (long int i = 0; i < no_cons; i++)
    {
        pthread_join(cons_id[i], NULL);
    }
    for (int i = 0; i < no_prod; i++)
    {
        pthread_join(prod_id[i], NULL);
    }
    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&data);
    return 0;
}
